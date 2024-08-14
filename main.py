#Main python file where the calculation happens
import numpy as np
variables_num=int(input("Enter the number of independent variables of your system of equations: "))
variables=[]
i=0
while i<variables_num:
    variables.append(f"X{i+1}")
    i+=1
print(variables)


#Creating matrix of coefficient of variables of each equation
def matrix_creator():
    global coeff_matrix
    global constant_matrix
    coeff_matrix=[]
    constant_matrix=[]
    #Filling coeff_matrix
    i=0
    while i<variables_num:
        j=0
        coeff_matrix.append([])
        while j<variables_num:
            coeff=int(input(f"Enter the coeffiecent no {j+1} of equation {i+1}: "))
            coeff_matrix[i].append(coeff)
            j+=1
        
        i+=1
    #Filling constant matrix
    k=0
    while k<variables_num:
        constant=int(input(f"Enter the constant of equation {k+1}: "))
        constant_matrix.append(constant)
        k+=1
    coeff_matrix=np.array(coeff_matrix)
    constant_matrix=np.array(constant_matrix)
#Will solve and return solution
def equation_solver(coeff_matrix,constant_matrix):
    global solutions
    solutions=[]
    i=0
    
    while i<variables_num:
        temp_matrix=coeff_matrix.copy()
        for element in temp_matrix:
            element[i]=constant_matrix[i]
        solution=format(float(np.linalg.det(temp_matrix)/np.linalg.det(coeff_matrix)),'0.2f')
        solutions.append(solution)
        i+=1
    
    print(solutions)

matrix_creator()
equation_solver(coeff_matrix,constant_matrix)

#Printing out the solution
for solution in solutions:
    print(solution)



