N = int(input())

star_list = ['*', '* *', '*****']

def make_star(n, arr):
    if n == N:
        return arr
    
    temp = []
    for i in range(n):
        temp.append(arr[i])
    
    for i in range(n):
        space_str = ' ' * ((n+i)*2 + 1 - 2*len(arr[i]))
        temp.append(arr[i] + space_str + arr[i])
    
    return make_star(2*n, temp)

def calibration(n, arr):
    for i in range(n):
        space_str = (n-1-i) * ' '
        arr[i] = space_str + arr[i] + space_str

star = make_star(3, star_list)
calibration(N, star)

for line in star:
    print(line)


#                        *                        
#                       * *                       
#                      *****                      
#                     *     *                     
#                    * *   * *                    
#                   ***** *****                   
#                  *           *                  
#                 * *         * *                 
#                *****       *****                
#               *     *     *     *               
#              * *   * *   * *   * *              
#             ***** ***** ***** *****             
#            *                       *            
#           * *                     * *           
#          *****                   *****          
#         *     *                 *     *         
#        * *   * *               * *   * *        
#       ***** *****             ***** *****       
#      *           *           *           *      
#     * *         * *         * *         * *     
#    *****       *****       *****       *****    
#   *     *     *     *     *     *     *     *   
#  * *   * *   * *   * *   * *   * *   * *   * *  
# ***** ***** ***** ***** ***** ***** ***** *****
