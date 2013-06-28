#!/usr/bin/env sh

# --------
# MySQL.sh
# --------

:<<'COMMENT'

% mysql -Version
mysql  Ver 14.14 Distrib 5.5.31, for debian-linux-gnu (x86_64) using readline 6.2
%



% mysql -h z -u <username> -p<password>
% mysql --host=z --user=<username> --password=<password>
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2069369
Server version: 5.1.69-0ubuntu0.10.04.1 (Ubuntu)

Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> quit
Bye
%



% cat ~/.my.cnf
[client]
host=z
user=<username>
password=<password>
%



% mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2069369
Server version: 5.1.69-0ubuntu0.10.04.1 (Ubuntu)

Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> quit
Bye
%



% mysql -v -H < ShowDatabases.sql > ShowDatabases.html
%

COMMENT
