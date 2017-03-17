# mysqlVerticalFormatToInsertQuery

A simple utility to convert mysql output into a insert command

## Example

Consider the following table output from repos_table

```
# assuming this is a mysql session
mysql> SELECT * from repos_table\G
*************************** 1. row ***************************
                    id: 1
             repo_name: mysqlVerticalFormatToInsertQuery
*************************** 2. row ***************************
                    id: 2
             repo_name: greb
```

If the above output is saved in a file named `default` and then on running
the script following will be produced

```
./convert.py repos_table
INSERT INTO repos_table (`id`, `repo_name`) VALUES (1, "mysqlVerticalFormatToInsertQuery"), (2, "greb");
```
