# G-Vault
**G-Vault** is a basic offline password manager with a command-line interface that saves sensitive information as _"data objects"_ to JSON files.
These data objects can contain: passwords, account info, payment methods (like credit cards, debit cards, etc.), email accounts, and more.
This is an early coding project and saves information unencrypted.

## Types of Data Objects
The data objects that **G-Vault** works with are linked to a corresponding category. The different data types that you can save using **G-Vault** contain different information fields.   
*When possible, some fields might be auto-filled based on the other fields provided with the data object.   
Unfilled fields that don't have enough information to be auto-filled are saved as null.*

#### Emphasis Key
* Unemphasized fields are just regular fields that don't have any requirements.
* _Italicized fields mean that at least one of the italicized fields is required to be provided._
* **_Bolded and Italicized fields mean that it is absolutely necessary for this field to be provided._**

### Accounts
Account data objects store login information about a service like local software or a website.   

Fields:
* **_Service:_** The name of the service that the account belongs to (ex. Adobe, Steam, Google, etc.)
* _Username:_ The username for this account.
* _Password:_ The password for this account.
* _Email:_ The email linked to this account.
* Phone: The phone number linked to the account.
* Security Questions: The security questions for this account.

### Addresses

### Documents

### Emails

### Payment Methods
