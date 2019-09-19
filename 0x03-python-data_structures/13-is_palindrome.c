#include "lists.h"
/**
 * is_palindrome - check if a linked list is palindrome
 * @head: head of the linked list
 * Return: 1 if linked list is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *auxh, *auxt;
	int flag = 0;

	if (*head == NULL)
		return (1);
	auxh = *head;
	auxt = *head;
	(*head)->prev = NULL;
	while (auxt)
	{
		if (auxt->next != NULL)
		{
			auxt = auxt->next;
			auxt->prev = auxh;
			auxh = auxh->next;
		}
		else if (auxt->next == NULL)
			break;
	}
	auxh = *head;
	while (auxt && auxh)
	{
		if (auxh->n != auxt->n)
			flag = 1;
		auxh = auxh->next;
		auxt = auxt->prev;
	}
	if (flag == 1)
		return (0);
	return (1);
}
