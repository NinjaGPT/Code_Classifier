## YARA Basic Knowledge
```
Install and Config: https://yara.readthedocs.io/en/v4.4.0/gettingstarted.html
Writing Yara Rules: https://yara.readthedocs.io/en/v4.4.0/writingrules.html
Open Source Rules : https://github.com/Yara-Rules/rules
Using from Python : https://yara.readthedocs.io/en/stable/yarapython.html
Regular Expression: https://javascript.info/regular-expressions, https://www.regular-expressions.info/
Malware Detection : https://www.sentinelone.com/blog/yara-hunting-for-code-reuse-doppelpaymer-ransomware-dridex-families/
```


###  Command Line:
```
chris@labs yara_rules % yara --help

YARA 4.3.2, the pattern matching swiss army knife.
Usage: yara [OPTION]... [NAMESPACE:]RULES_FILE... FILE | DIR | PID

Mandatory arguments to long options are mandatory for short options too.

       --atom-quality-table=FILE           path to a file with the atom quality table
  -C,  --compiled-rules                    load compiled rules
  -c,  --count                             print only number of matches
  -d,  --define=VAR=VALUE                  define external variable
       --fail-on-warnings                  fail on warnings
  -f,  --fast-scan                         fast matching mode
  -h,  --help                              show this help and exit
  -i,  --identifier=IDENTIFIER             print only rules named IDENTIFIER
       --max-process-memory-chunk=NUMBER   set maximum chunk size while reading process memory (default=1073741824)
  -l,  --max-rules=NUMBER                  abort scanning after matching a NUMBER of rules
       --max-strings-per-rule=NUMBER       set maximum number of strings per rule (default=10000)
  -x,  --module-data=MODULE=FILE           pass FILE's content as extra data to MODULE
  -n,  --negate                            print only not satisfied rules (negate)
  -N,  --no-follow-symlinks                do not follow symlinks when scanning
  -w,  --no-warnings                       disable warnings
  -m,  --print-meta                        print metadata
  -D,  --print-module-data                 print module data
  -M,  --module-names                      show module names
  -e,  --print-namespace                   print rules' namespace
  -S,  --print-stats                       print rules' statistics
  -s,  --print-strings                     print matching strings
  -L,  --print-string-length               print length of matched strings
  -X,  --print-xor-key                     print xor key and plaintext of matched strings
  -g,  --print-tags                        print tags
  -r,  --recursive                         recursively search directories
       --scan-list                         scan files listed in FILE, one per line
  -z,  --skip-larger=NUMBER                skip files larger than the given size when scanning a directory
  -k,  --stack-size=SLOTS                  set maximum stack size (default=16384)
  -t,  --tag=TAG                           print only rules tagged as TAG
  -p,  --threads=NUMBER                    use the specified NUMBER of threads to scan a directory
  -a,  --timeout=SECONDS                   abort scanning after the given number of SECONDS
  -v,  --version                           show version information

Send bug reports and suggestions to: vmalvarez@virustotal.com.

```
#### -t,  --tag=TAG   
>In the YARA command line, the -t argument is used to specify TAG so that only the rules that match the given TAGs are printed and the rest are ignored. Here are some examples of using the -t parameter:

>Apply rules with specific TAGs:
If you want to apply the rules defined in /foo/bar/rules to a file named bazfile, but only want to report the rules tagged as "Packer" or "Compiler", you can use the following command:
```
yara -t Packer -t Compiler /foo/bar/rules malware
```
>This command executes the rules in the /foo/bar/rules file, but only reports the results of those rules tagged as "Packer" or "Compiler".
Using the -t parameter helps you filter and focus on specific types of threats or characteristics, making the analysis more efficient and targeted. This is especially useful when dealing with a large number of YARA rules and different types of malware.
 
### A simple rule:
```
chris@labs yara_rules % cat rule1.yar
rule find_mysql:sqli
{
	meta:
		author = "Chris"
		description = "find keyword mysql"
	strings:
		$str1 = "mysql" nocase

	condition:
		$str1
}
chris@labs yara_rules % yara -r -s rule1.yar ../../Java_Vulns/sql_injection/mysql/delete/Statement
find_mysql ../../Java_Vulns/sql_injection/mysql/delete/Statement/where_string.md
0x8:$str1: MySQL
0x35:$str1: MySQL
0x67:$str1: mysql
0x316:$str1: mysql
0x3cd:$str1: mysql
0x75c:$str1: MySQL
find_mysql ../../Java_Vulns/sql_injection/mysql/delete/Statement/where_integer.md
0x8:$str1: MySQL
0x35:$str1: MySQL
0x67:$str1: mysql
0x84a:$str1: MySQL
0x9e1:$str1: MySQL


```
### Basic Knowledge:
```
BASIC STRUCTURE:

rule RULE_NAME [TAG_NAME]
{
	meta:
		author = "Chris"
	strings:
		$str = "string, hex, regular expr, etc"
	condition"
		$str //if match, return true

}


meta: information of current rule, such as author, description, etc, will not be executed.

strings: defined strings, also can be HEX, Regular Expression, will be used in 'condition'.

condition: define the conditions to match.

comment: C style, multiple lines use /* xxx */, single line use // xxx
```
* String Types:
```
$STR = {FF FF FF} // Hex Strings.

$STR = "Text Strings" //Text Strings.

$STR = /md5: [0-9a-zA-Z]{32}/  //RegExpr Strings.
```

* HEX Strings:
```
* wild-cards:		?	e.g:	$str = { FF ?F ?? 08 4D }  // means FF XF XX 08 4D

* not operator:		~	e.g:	$str = { FF ~00 4D }// means FF non-00 4D

* MIXED USE:		~?	e.g:	$str = { F4 23 ~?0 6D } // means F4 23 non-X0 6D

* jump operator:	-	e.g:	$str = { F4 23 [4-6] 62 B4 } //means 4 to 6 bytes

/* 
all of below will be matched, 
but remember [X-Y] must follow 0 <= X <= Y
if the number of byte can be confirmed, just [X] also ok

F4 23 01 02 03 04 62 B4
F4 23 00 00 00 00 00 62 B4
F4 23 15 82 A3 04 45 22 62 B4
*/

* unbounded jumps:	-	e.g:	$str = { FE 39 45 [10-] 89 00 } //means min 10 bytes, infinite
					$str = { FE 39 45 [-] 89 00 }.  //means 0 byte to infinite

* OR operator:		|	e.g:	$str = { F4 23 ( 62 B4 | 56 ) 45 } //"F4 23 62 B4 45" or "F4 23 56 45"


```

* TEXT Strings:
```
$STR = "chris is handsome"	//simplest case, ASCII-encoded, case-sensitive.

/*
can also contain the following subset of the escape sequences available:

\"	Double quote
\\	Backslash
\r	Carriage return
\t	Horizontal tab
\n	New line
\xdd	Any byte in hexadecimal notation

*/

* case-insensitive:	nocase	$str = "chris is handsome" nocase //ignore case, like ChRis Is HaNdSome

* wide-char strings:	wide	$str = "Bordland" wide //two bytes per char (00 + ASCII), \x00a\x00b

* XOR strings:		xor	$str = "This program cannot" xor // every single byte XOR applied

* MIXED USE:	wide ascii xor $str = "This program cannot" xor wide ascii

* XOR range:	xor(min-max)	$str = "This program cannot" xor(0x01-0xff)

* base64 strings:	base64	$str = "this program connot" base64 //will match 3 permutations

* base64wide:		base64wide //convert base64 to wide

* fullword:		fullword //Searching for full words

```

* Regular expressions
```
$re1 = /foo/i    // This regexp is case-insentitive, equals /foo/ nocase, recommend latter
$re2 = /bar./s   // In this regexp the dot matches everything, including new-line
$re3 = /baz./is  // Both modifiers can be used together


```
* private strings:	
```
private		//which means they will never be included in the output
```
* Unreferenced strings:
```
$_unreferenced = "AXSERS" //If a string identifier starts with an _ then it does not have to be referenced in the condition
```

#### String Modifier Summary
```
https://yara.readthedocs.io/en/latest/writingrules.html#string-modifier-summary

```


### Conditions
> Operators' description:
https://yara.readthedocs.io/en/latest/writingrules.html#conditions

* String identifiers are acting as Boolean variables

```
    condition:
        ($a or $b) and ($c or $d)
```
* Counting strings, # with variable name means the number of occurrences of each string
```
    condition:
        #a == 6 and #b > 10
```
* the count of a string in an integer range
```
	#a in (filesize-500..filesize) == 2

//In this example the number of 'a' strings in the last 500 bytes of the file must equal exactly 2.

```
* string offsets or virtual addresses
```
    condition:
        $a in (0..100) and $b in (100..filesize)

//the string $a must be found at an offset between 0 and 100, while string $b must be at an offset between 100 and the end of the file.
```

* SETS of STRINGS
>https://yara.readthedocs.io/en/latest/writingrules.html#sets-of-strings-1
```
2 of ($a,$b,$c)

2 of ($foo*)  // equivalent to 2 of ($foo1,$foo2,$foo3)

3 of ($foo*,$bar1,$bar2)

1 of them // equivalent to 1 of ($*)

all of them       // all strings in the rule
any of them       // any string in the rule
all of ($a*)      // all strings whose identifier starts by $a
any of ($a,$b,$c) // any of $a, $b or $c
1 of ($*)         // same that "any of them"
none of ($b*)     // zero of the set of strings that start with "$b"
```
* Same Condition to many strings
>https://yara.readthedocs.io/en/latest/writingrules.html#applying-the-same-condition-to-many-strings

#### for expression of string_set : ( boolean_expression )
```
And its meaning is: from those strings in string_set at least expression of them must satisfy boolean_expression.

In other words: boolean_expression is evaluated for every string in string_set and there must be at least expression of them returning True.

use a dollar sign ($) as a place-holder 

for any of ($a,$b,$c) : ( $ )

for all of them : ( # > 3 )

for all of ($a*) : ( @ > @b )

```
* anonymous string with 'of'
```
    strings:
        $ = "dummy1"
        $ = "dummy2"

    condition:
        1 of them
```
* for ... in
```
for any k,v in some_dict : ( k == "foo" and v == "bar" )


for <quantifier> <variables> in <iterable> : ( <some condition using the loop variables> )

Where <quantifier> is either any, all or an expression that evaluates to the number of items in the iterator that must satisfy the condition, <variables> is a comma-separated list of variable names that holds the values for the current item (the number of variables depend on the type of <iterable>) and <iterable> is something that can be iterated.


```
* Referencing other rules
```
$a and Rule1

any of (Rule*)
```






