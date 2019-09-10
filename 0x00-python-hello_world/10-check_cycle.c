#include "lists.h"
/**
 * check_cycle - Searche for loop inside a list
 * @list: Head of the linked list
 * Return: 1 if there is a cycle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);
	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
