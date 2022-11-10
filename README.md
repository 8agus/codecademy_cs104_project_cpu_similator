# CPU Similator 

## Project Ideas

Ideas for what program can accomplish:

1.  Create program that mimic the functionalities of a CPU, cache, and memory bus
2.  Fetch and parse instructions from an input file
3.  Fetch and parse initialization values for the Memory Bus from a separate input file
4.  Send CPU instructions and initial Memory Bus values to the CPU and Memory Bus, respectively
5.  Provide console output to the user documenting the stages of input processing
6.  Implement an ISA that can handle MIPS Instructions such as the following:

## Implementation: 

Execute in CLI to initiate program: python3 main.py instruction_input.txt data_input.txt

### Functions

  #### * read_instructions()
  
    Function accept one argument and is the only function call to initialize the programm. 
    
    The argument is variable 'open_instr' that accesses the instructions.txt file to delegate operations to other functions. 
    
    First the information is broken up line for line and thereafter in the smaller chucks by spliting on ','.
    
    Example: 
    
    step 1: 'ADDI,R2,R2,2'
    step 2: 'ADDI', 'R2', 'R2','2'
    
    The first chuck of new line contains the operant the indicates the operation that needs to be done on the remainder of the instructions. 
    Using [if] and [elif] statements each line is directed to the respective functions to process instructions 
    [else] if first chuck of code is not delegated an error message is printed "ERROR - Invalid instructions received: " with the line of 
    instructions received. 


  #### * cache()
  
    Function accept one argument. 

    [if] the argument is '1' then a print statement "Memory before loading: " is made of empty dictionary that represent empty Memory Register. 
    Using a for loop information is retrieved from variable 'open_data' to populate data into dictionary 'memo_reg' and then
    dictonary is printed to similate information has been loaded to Memory register 

    [else] statement is printed "Memory before halt: " with information contained in dictionary 'memo_reg'. The dictionary is then cleared using and 
    statement printed "Memory after HALT: " as console output to the user documenting clearing of memory. 


  #### * addi()
  
    Functions takes one argument that contain the line of instructions received from read_instructions() and below 2 lines are prineted:
    
      "Addi Function initiated " to indicate process has started 
    
      "Opcode received in ADDI: " with the line of instructions. Example 'ADDI', 'R2', 'R2','2'.
      
      R2 = R2 + 2
      
      'R2' : Destination in Memory Register where answer to equation needs to be stored  
      'R2' : Source location from where value should be retrieved from Memory Register 
      '2'  : Int value to be added in equation  
    
    Call is made to value_from_cache() with R2 as argument to retrieve the value in that location and returned value is saved to variable 'value_1'
    Add equition is then performed with value in 'value_1' plus 2 and saved to variable 'answer'
    Call is then made to write_to_register() with agruments 'R2' as 'dest and answer as value to update register
    
    The following 2 statements are then printed: 
    
    "The answer for {value_1[0]} + {value_2} is: {answer}" - console output to the user documenting the 2 values and answer to equation.
    "Addi Function completed successfully" - console output to the user documenting operation has been completed.


  #### * add()

    
    Functions takes one argument that contain the line of instructions received from read_instructions() and below 2 lines are prineted:
    
      "Add Function initiated " to indicate process has started 
    
      "Opcode received in ADD: " with the line of instructions. Example 'ADD', 'R3', 'R2', 'R1'.
      
      R3 = R2 + R1
      
      'R3' : Destination in Memory Register where answer to equation needs to be stored  
      'R2' : Source location from where value should be retrieved from Memory Register 
      'R3' : Source location from where value should be retrieved from Memory Register 
    
    Call is made to value_from_cache() with R2 and R3 as argument to retrieve the values in locations and returned values is saved to variable 'value'
    and reg_add. 
    Add equation is then performed with the 2 values in variable 'value' and saved to variable 'answer'
    Call is then made to write_to_register() with agruments 'R3' as 'dest and answer as value to update Memory Register
    
    The following 2 statements are then printed: 
    
    "The answer for {value[0]} + {value[1]} is: {answer}" - Console output to the user documenting the 2 values and answer to equation.
    "Add Function completed successfully" - Console output to the user documentingoperation has been completed.
    
  #### * jump()
  
    Functions takes one argument that contain the line of instructions received from read_instructions() and below 2 lines are prineted:
    
      "Jump Function initiated" - to indicate process has started 
      "Opcode received in jump: " - with the line of instructions. Example 'J', '8'.
      
    The purpose is only to simulation output by randomly selecting a number between 0 and 6, which is saved to variable 'select_jump'.
    'select_jump' is then used as an index to retrieve key/value from dictionary 'memo_reg'. 
    
    The following two lines are then printed out: 
    
      "Using Jump function register went to register address {register} with Value {value}" - to similate there was a jump to another Memory             Register location.
      "Jump Function completed successfully" - Console output to the user documenting operation has been completed.

  #### * value_from_cache()
  
    Function takes a list as argument and the list would contain keys to access values in variable 'loca_address'. 
    
    Below message is printed out to similate operation has started:
    
      "Retrieving information from register initiated"

    A for loop is used to retrieve keys from argument list and the value in variable 'local_address' would provide index position
    This index positions are then used to retrieve Memory Register location in variable 'memo_reg' and append to list in variable values.
    
    Below statement is then printed out:
    
      "Retrieved value is {values} from location {register}." - Console output to the user documenting the information retrieved 
      "Information successfully retrieved" - Console output to the user documenting process has been successful
      "Information sent to Operand" - Console output to the user documenting location/value has been sent to Operation Function 

  #### * write_to_register()

    Function takes the following two arguments: 

    1. value_in: Containts the value that needs to be updated in dictionary 'memo_reg'
    2. reg_loc_in: Contains the location information where value needs to be updated in dictionary 'memo_reg'

    A statement is printed "Write to register initiated" to simbolize process has started and then
    the dictionary is printed before making changes. 

    Call is then made to value_from_cache() using 'reg_loc_in' as argument to find the location address and saves it to variable 'reg_address'.
    Variable 'reg_address' then contains the key that will be used to update 'value_in' in dictionary 'memo_reg'. 

    The dictionary is printed again to similate change has been made to Register Memory and line is printed "Register update successfully" to 
    similate operation has been completed.

  #### * time_delay()
  
    Used a 4 second delay on concole output in order for user to read as ISA instructions are being processed. 

### Variables 

  #### * open_date
  
    Used to save information retrieved from data_input.txt file
  
  #### * open_instr
  
    Used to save information retrieved from instructions_input.txt file
  
  #### * memo_reg
  
    Dictionary list used to link ISA/MIPS instruction with Memory Location imported from data_input.txt file.
    The MIPS Destination or Source Register is linked to each line in data_input.txt file by index position. 
    
    Example: 
      > Line 1 in 'data_input.txt' file is location '00000001' with value '4' at index 0 and MIPS 'R1' (Key) is also index 0 (value).   
      > Line 2 in 'data_input.txt' file is location '00000010' with value '5' at index 1 and MIPS 'R2' (Key) is also index 1 (value).
     
  #### * local_address
  
    Dictionary list used to to represent location of a value in Memory Register of CPU.  
    First line of data_input.txt file reads as '00000001,4', which is interpreted as '00000001' (Key) being location address of value '4' (value). 
    
 Requirements
 
 * sys
 * time 
 * random
    

