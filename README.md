# infra-nat

Does these things:

- nat server

Setup as usual:

```bash
$ git clone --recursive git@github.com:balanced-cookbooks/infra-global.git
$ cd infra-nat
$ mkvirtualenv infra-nat
(infra-global)$ pip install -r requirements.txt 
```

## Local development

(infra-nat)$ vagrant up nat

## Build and publish config

NOTE: You must do this on a machine with the same architecture as what you're about to deploy to.

If you are on OSX run the following commands

```bash
(infra-nat)$ pypi_username=user pypi_password=pass vagrant provision infra-nat
(infra-nat)$ vagrant ssh -c ""source ~/infra/bin/activate && cd ~/infra-nat/ && confu pkg clean && confu pkg build"
(infra-nat)$ confu pkg upload
```

to see what we've released:

```bash
(infra-nat)$ confu pkg pubd
```


## Launch a stack

```bash
$ confu cfn create formations/nat.py ConfVer=f26fa6d KeyName=your-aws-ssh-key-name
```
