import javalang
import sys


fileName = ''
methodName = ''
java_code = ''

try:
	if len(sys.argv)==3:
		fileName = sys.argv[1]
		methodName = sys.argv[2]
		fd = open(fileName,"r",encoding="utf-8")
		java_code = fd.read()
		fd.close()
	else:
		print("Usage: ",sys.argv[0],"<CodeFile>  <MethodName>")
		exit()
except FileNotFoundError:
		print("Cannot find file ",fileName)
		exit()

def extract_method_code(java_code, method_name):
    # Parse the Java code into an AST
    tree = javalang.parse.parse(java_code)

    start_line = None
    end_line = None
    extract = False

    # Traverse the AST to find the start and end of the method
    for _, node in tree:
        if isinstance(node, javalang.tree.MethodDeclaration) and node.name == method_name:
            # Start extracting when the target method is found
            start_line = node.position.line if node.position else None
            extract = True
        elif extract and (isinstance(node, javalang.tree.MethodDeclaration) or isinstance(node, javalang.tree.ClassDeclaration)):
            # Stop extracting when the next method or class is found
            end_line = node.position.line if node.position else None
            break

    # Extract the method code from the original source
    if start_line and end_line:
        lines = java_code.split('\n')
        method_code_lines = lines[start_line-1:end_line-1]
        return '\n'.join(method_code_lines)
    
    return None  # Return None if the method is not found



# Example usage:


# Extract the prototype of 'myMethod'
try:
	method_prototype = extract_method_code(java_code, methodName)
	if method_prototype == None:
		print("Cannot find Mehotd ",methodName)
		exit()
	else:
		print(method_prototype)
except:
	exit()
