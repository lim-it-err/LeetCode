/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeKLists(struct ListNode** lists, int listsSize){
    struct ListNode* answer = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* head = answer;
    int LIST_LEFT = listsSize;
    //check NULL
    for(int i =0 ; i < listsSize;i++) if(lists[i]==NULL) LIST_LEFT--;
    if(LIST_LEFT==0) return NULL;
    while(LIST_LEFT)
    {
        int min = 1000000; int min_idx = -1;
        for(int i = 0 ; i < listsSize; i++)
        {
            if(lists[i]!=NULL)
            {
                if(lists[i]->val < min)
                {
                    min = lists[i]->val;
                    min_idx = i;
                }
            }
        }//traversed all index
        head->val = min;
        head->next = malloc(sizeof(struct ListNode));
        if(lists[min_idx]->next!=NULL)lists[min_idx]=lists[min_idx]->next;
        else                    {lists[min_idx]=NULL; LIST_LEFT--;}
        if(LIST_LEFT>=1) head = head->next;
        
    }
    head->next = NULL;
    return answer;
}