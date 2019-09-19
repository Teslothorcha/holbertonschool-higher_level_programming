#include "lists.h"
/**
 * is_palindrome - check if a linked list is palindrome
 * @head: head of the linked list
 * Return: 1 if linked list is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *auxh = *head, *auxt = *head;

	if (*head == NULL)
		return (1);
	(*head)->prev = NULL;
	while (auxt)
	{
		if (auxt->next == NULL)
		{
			break;
		}
		else
		{
			auxt = auxt->next;
			auxt->prev = auxh;
			auxh = auxh->next;
		}
	}
	auxh = *head;
	while (auxt && auxh)
	{
		if (auxh->n != auxt->n)
			return(0);
		auxh = auxh->next;
		auxt = auxt->prev;
	}
	return (1);
}
