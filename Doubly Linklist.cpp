#include <stdio.h>
#include <stdlib.h>

struct student *head,*tail;
struct student
{
    int roll;
    struct student *prev;
    struct student *next;
};

void create()
{
    struct student *p,*q = head;
    p = (struct student *)malloc(sizeof(struct student *));
    printf("\nEnter Roll:");
    scanf("%d",&p->roll);
    p->next = NULL;
    p->prev = NULL;
    if(head==NULL)
    {
        head = p;
        tail = p;
    }
    else
    {
        p->prev = tail;
        tail->next = p;
        tail = p;
    }
}

void display()
{
    struct student *p = head;
    while(p!=NULL)
    {
        printf("Roll is:%d\n",p->roll);
        p = p->next;
    }
}
void insert(int pos)
{
    struct student *p,*q = head;
    int c = 1;
    p = (struct student *)malloc(sizeof(struct student));
    printf("\nEnter Roll:");
    scanf("%d",&p->roll);
    if(pos==1)
    {
        p->next = head;
        head->prev = p;
        p->prev = NULL;
        head = p;
    }
    else
    {
        while(c<pos-1)
        {
            q = q->next;
            c++;
        }
        if(q->next==NULL)
        {
            p->prev = q;
            q->next = p;
            tail = p;
            p->next = NULL;
        }
        else
        {
            p->prev = q;
            q->next->prev = p;
            p->next = q->next;
            q->next = p;
        }
    }
}
void delete(int pos)
{
    struct student *q = head,*t;
    int c = 1;
    if(pos==1)
    {
        head = q->next;
        free(q);
    }
    else
    {
        while(c<pos-1)
        {
            q = q->next;
            c++;
        }
        t = q->next;
        q->next = q->next->next;
        if(t->next==NULL)
            tail = q;
        free(t);
    }
}
void reverse()
{
    struct student *p=tail;
	while(p!=NULL)
	{
	    printf("Roll no is:%d\n",p->roll);
		p = p->prev;
	}
}

int main()
{
    int ch,pos;
    head = tail = NULL;
    while(1)
    {
        printf("\nEnter 1 to create:\n2 to display:\n3 to insert at a particular position:\n4 to delete:\n5  to display in reverse:\n6 to exit: ");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:
                create();
                break;
            case 2:
                display();
                break;
            case 3:
                printf("Enter the position:");
                scanf("%d",&pos);
                insert(pos);
                break;
            case 4:
                printf("Enter the position:");
                scanf("%d",&pos);
                delete(pos);
                break;
            case 5:
                reverse();
                break;
            case 6:
                exit(0);
            default:
                printf("Wrong choice");
        }
    }
    return 0;
}
