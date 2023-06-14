        #include <stdio.h>
        #include <stdlib.h>
         
        main (void){
            
            int resto,w;
            
            scanf("%d",&w);
            
            resto = w/2;
            
            if (resto==0){
                printf("YES\n");
            } else {
                printf("NO\n");
            }
            
            return 0;
        }