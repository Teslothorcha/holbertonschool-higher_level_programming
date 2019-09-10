#include "lists.h"
/**
 * check_cycle - Searche for loop inside a list
 * @list: Head of the linked list
 * Return: 1 if there is a cycle else 0
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast_p->next)
	{
		slow = slow_p->next;
		fast = fast_p->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
