# ERC20_SmartContract_Generator
## Project Summary
This is a python project that uses an erc20.sol smart contract template I created to generate an erc20 smart contract when running the program.

# Steps in Running the Application
## Step 1:
 - Prerequisites:
   - Install Python
   - Install PyCharm
   - Solidity Plugins (within the PyCharm IDE)

## Step 2:
 - Run the application
 - Application will ask the user multiple questions for user input to place in {} within the erc20.sol template
 - Then whatever the user decides the name of the .sol file to be generated a .sol erc20 contract will be generated.

# Considerations
This is a basic erc20 contract that will be generated, it has not been audited, and there are other considerations to add to the contract that will be generated. While there is a minter there is no constructor for the minter function. This was purely for fun, and learning purposes. I plan on adding and upgrading the capabilities, and adding more universal and detailed inputs to the contract generation for a more robust and descriptive smart contract generation. Next update I will add a GUI using tkinter. I hope this helps people slowly into the world of blockchain and solidity.
