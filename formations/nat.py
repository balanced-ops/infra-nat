#!/usr/bin/env python
from __future__ import unicode_literals

from confu import atlas
from troposphere import (
    Template, FindInMap, GetAtt, Ref, Parameter, Join, Base64, Select, Output,
    ec2, autoscaling as asg, elasticloadbalancing as elb
)
from troposphere.cloudformation import WaitCondition, WaitConditionHandle


template = Template()

template.add_description('nat')

atlas.infra_params(template)

atlas.conf_params(template)

atlas.instance_params(
    template,
    roles_default=['nat',],
    iam_default='nat',
)

atlas.scaling_params(template)

atlas.mappings(
    template,
    accounts=[atlas.poundpay],
)

atlas.has_zone_condition(template)

i_secgrp = atlas.instance_secgrp(
    template,
    SecurityGroupIngress=[
        ec2.SecurityGroupRule(
            'NATALL',
            IpProtocol='-1',
            FromPort='-1',
            ToPort='-1',
            CidrIp='0.0.0.0/0',
        ),
    ]
)

i_meta_data = {}
atlas.cfn_auth_metadata(i_meta_data)
atlas.cfn_init_metadata(i_meta_data)

i_user_data = Join(
    '',
    atlas.user_data('NATLaunchConfiguration') +
    atlas.user_data_signal_on_scaling_failure(),
)

i_launchconf = atlas.instance_launchconf(
    template,
    'NAT',
    UserData=Base64(i_user_data),
    Metadata=i_meta_data,
    SecurityGroups=[Ref(i_secgrp)],
)


if __name__ == '__main__':
    print template.to_json(indent=4, sort_keys=True)
