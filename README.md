# Cova Dispensary POS Audit Tools
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/audit-tools?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/audit-tools?style=for-the-badge)

An inventory audit tool for speeding up inventory and avoiding errors that occur during processing. This tool will allow
users to complete inventory counts with a simple workflow that remedies user error.


Installation and Usage
-----
```bash
$ pypi install audit-tools
```

```python
from audit_tools import SessionManager, Scanner

session = SessionManager('/path/to/products.csv') # Path to products.csv
scanner = Scanner(session) # Create a scanner object

...

session.count_product('F7X6A7', 20) # Add 20 of F7X6A7 to the inventory
session.reduce_product('F7X6A7', 3) # Reduce 3 of F7X6A7 from the inventory

...

scanner.start_count() # Starts a text based loop for counting products

session.shutdown() # Parses session data and saves the session to a file
```


Problems
--------
All the problems that we encounter while processing inventory data during an audit.

* Extremely slow
* Miscounts often occur
* Redundant item checks
* Manual data entry
* User error

Solutions
---------
Our ideas for solution implementations for fixing these problems so that an Audit can be completed successfully with
accuracy and speed.

- #### Session Manager
    - Allows users to start a new session with a products csv or xlsx file. The session manager will process all incoming
    products and append them to the sessions DataFrame, when you shut down the session manager will parse all the data in the session, complete variance calculations, raise any alerts, and save the session to the updated csv
    or xlsx file.


- #### Scan & Count
    - Allows users to scan a SKU and count the number of products to update the session file.


- #### Scan & Edit
    - Allows user to scan a SKU adn manage the data entry for a specified product in the session.


- #### Receipt Parser
    - Allows user to upload scan a receipt and the system will parse the receipt and update the session file.

Feature List
------------
This list will include all the features, current and future.

|    Features     | Working Status |
|:---------------:|:--------------:|
| Session Manager | In Development |
|  Scan & Count   |    Planned     |
|   Scan & Edit   |    Planned     |
| Receipt Parser  |    Planned     |



Dev notes:
If you come across this project, I am a newish developer, and I am not familiar with the 
python ecosystem especially poetry. If you are confused on the namings in this project, keep in mind
this package was created for a sole reason to help the creator at work, and will be used in tandem with
a handheld scanner.