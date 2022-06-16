# SI504 Homework 6

Hi Jack,



I'm sorry to hear you got injured, take care and hope you would recover soon. 



1. I used the command **ssh-keygen -t rsa** to generate the key pair.  The generated public key is also shown below. 

   ```
   ruiding@ip-172-31-70-98:~$ ssh-keygen -t rsa
   Generating public/private rsa key pair.
   Enter file in which to save the key (/home/ruiding/.ssh/id_rsa):
   Created directory '/home/ruiding/.ssh'.
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
   Your identification has been saved in /home/ruiding/.ssh/id_rsa
   Your public key has been saved in /home/ruiding/.ssh/id_rsa.pub
   The key fingerprint is:
   SHA256:vBzE4XGLhnRBFGANNZVoJRO4+woxgRfbvU+wsrcqCoo ruiding@ip-172-31-70-98
   The key's randomart image is:
   +---[RSA 3072]----+
   |    . =O#B+.     |
   |   . *.*+O..     |
   |  . + ooO .      |
   |   . ..+ +       |
   |    o ..S .      |
   |     o.+ =       |
   |.   . ..+ .      |
   |o.  .. ...       |
   |E .. .oo.        |
   +----[SHA256]-----+
   ruiding@ip-172-31-70-98:~$ cat ./.ssh/id_rsa.pub
   
   
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDEyxxsY9B3oFvw7vSt+rcDU49a3ryJ9SpcWj89cbBMjytjjXn2oquD/1Xse5qyu+OsnWqNpsu6sxZBABO0BvYCaI3V2mlGq9+exa1z+B/gCQ4S/4/suKB8S2dFuhmCxA/FwsEbbOsByuOpve1AjId7bMnwm4hy9FJIdPoAeXL8vaQP+NbA3Rw3r9TUB1f/yHQglXrELVEM63/A+ifbr539kVJihF0cE+L1uJ7PQppYri22gPOXY4BXTJbVvsL5f/aHNAybKf0+Tpbl/vp5kWeoAbf6fWY73zvReiaXX/mh99eW6Q9vjzykGj4VKeDQU4AZWzgk3LOCQllLlgnmGAe991qMrTVyc+GOa6fy+qr/Tm79aEdlmKtVMUKgqnVamIMIlW/KqQKkqExt6UCF4PMkx1Pi1bPz0bpe9Vte6GRNuFnRIlSO4T0b8AVF7GPkKDKHiywdJX8ojmom2Te4SoZCUurLaq3QaB+47OnOcnP5Wl9ETLxskjcEChj4TSi60EU= ruiding@ip-172-31-70-98
   ```

2. I used the command **sudo apt-get install apache2** to install apache2.

   ```
   ruiding@ip-172-31-70-98:~$ sudo apt-get install apache2
   [sudo] password for ruiding:
   Reading package lists... Done
   Building dependency tree
   Reading state information... Done
   The following additional packages will be installed:
     apache2-bin apache2-data apache2-utils libapr1 libaprutil1
     libaprutil1-dbd-sqlite3 libaprutil1-ldap libjansson4 liblua5.2-0 ssl-cert
   Suggested packages:
     apache2-doc apache2-suexec-pristine | apache2-suexec-custom www-browser
     openssl-blacklist
   The following NEW packages will be installed:
     apache2 apache2-bin apache2-data apache2-utils libapr1 libaprutil1
     libaprutil1-dbd-sqlite3 libaprutil1-ldap libjansson4 liblua5.2-0 ssl-cert
   0 upgraded, 11 newly installed, 0 to remove and 171 not upgraded.
   Need to get 1865 kB of archives.
   After this operation, 8091 kB of additional disk space will be used.
   Do you want to continue? [Y/n] y
   ```

   The default page looked like this:

   ![image-20220306122214890](C:\Users\dingr\AppData\Roaming\Typora\typora-user-images\image-20220306122214890.png)

​		The I used the command **sudo wget https://github.com/SI504/basic_html/raw/master/zip.zip** to download the zip file. 

```
ruiding@ip-172-31-70-98:/var/www/html$ sudo wget https://github.com/SI504/basic_html/raw/master/zip.zip
[sudo] password for ruiding:
--2022-03-06 17:41:02--  https://github.com/SI504/basic_html/raw/master/zip.zip
Resolving github.com (github.com)... 140.82.114.4
Connecting to github.com (github.com)|140.82.114.4|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://raw.githubusercontent.com/SI504/basic_html/master/zip.zip [following]
--2022-03-06 17:41:02--  https://raw.githubusercontent.com/SI504/basic_html/master/zip.zip
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 117586 (115K) [application/zip]
Saving to: ‘zip.zip’

zip.zip             100%[===================>] 114.83K  --.-KB/s    in 0.003s

2022-03-06 17:41:03 (34.0 MB/s) - ‘zip.zip’ saved [117586/117586]

ruiding@ip-172-31-70-98:/var/www/html$ ls
index.html  zip.zip
ruiding@ip-172-31-70-98:/var/www/html$ sudo unzip zip.zip
Archive:  zip.zip
replace index.html? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: index.html
   creating: w3images/
  inflating: w3images/forestbridge.jpg
```

The page after replacement looked like this:

![image-20220306124436710](C:\Users\dingr\AppData\Roaming\Typora\typora-user-images\image-20220306124436710.png)

3. I used the command **sudo cp -r ~ /root** to backup in root's home directory.  I have to use **sudo** since the destination file directory is /root . I used -r to recursively copy all the files under my home directory. 

```

ruiding@ip-172-31-70-98:~$ sudo cp -r ~ /root
ruiding@ip-172-31-70-98:~$ sudo ls /root
ruiding  snap
```



If you have any concern, feel free to contact me!

Best Regard,

Rui