# NAT role for VPC

If you are on OSX run the following commands

```bash
(infra-vault)$ pypi_username=ttt pypi_password=foo vagrant provision
(infra-vault)$ vagrant ssh -c "source ~/infra/bin/activate && cd ~/infra-nat/ && confu pkg clean && confu pkg build"
(infra-vault)$ confu pkg upload
```
