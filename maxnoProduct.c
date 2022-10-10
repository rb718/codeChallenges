#include <stdio.h>

int main()
{
    int i, n, j, begin, end, noProduct = 0, maxnoProduct = 0, maxBegin, maxEnd;
    printf("Please enter total number of piles: ");
    scanf("%d", &n);
    int numProducts[n];
    printf("---Enter no. of products in pile---\n");
    for(i = 0; i < n; i++)
    {
        scanf("%d", &numProducts[i]);    
    }
    //finding the sub array with strictly increasing sub-arrays
    begin = end = 0;
    for(i = 0; i < n - 1; i++)
    {
        if(numProducts[i] < numProducts[i + 1])
        {
            end = i + 1;
            //printf("Begin: %d END: %d\n", begin, end);
        }
        else
        {
        	noProduct = 0;
        	for(j = begin; j <= end; j++)
        	{
        		noProduct = noProduct + numProducts[j]; 	
			}
            //noPile = end - begin + 1;
            //printf("Begin: %d End: %d\n", begin, end);
            if(maxnoProduct < noProduct)
            {
                maxnoProduct = noProduct;
                maxBegin = begin;
                maxEnd = end;
            }
            begin = i + 1;
        }
    }
    //this is the longest increasing sub-array appears at last
    noProduct = 0;
    for(j = begin; j <= end; j++)
    {
        noProduct = noProduct + numProducts[j]; 	
	}
    if(maxnoProduct < noProduct)
    {
        maxnoProduct = noProduct;
        maxBegin = begin;
        maxEnd = end;
    }
    printf("Maximum number of products: %d\n", maxnoProduct);
    //scanf("%d", &j);
    printf("---Products Picked---\n");
    for(i = maxBegin; i <= maxEnd; i++)
        printf("%d ", numProducts[i]);
    return 0;
}