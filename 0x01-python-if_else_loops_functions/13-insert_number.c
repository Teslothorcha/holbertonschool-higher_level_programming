#include "lists.h"
/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *step1 = *head, *step2 = *head;
	int flag, flagg;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (step1->next != NULL)
		{
			step2 = step1->next;
			if (number > step1->n)
				flag = 1;
			if (number < step1->n)
			{
				flagg = 1;
			}
			else if (step1->n <= number && step2->n >= number)
			{
				step1->next = new;
				new->next = step2;
				flag = 0;
				break;
			}
			step1 = step1->next;
		}
		if (flag == 1)
			add_nodeint_end(&*head, number);
		if (flagg == 1)
		{
			new->next = *head;
			*head = new;
		}
	}
	return (new);
}
