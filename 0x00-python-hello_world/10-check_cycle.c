#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in the linked list
 * @list: pointer to list to be freed
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *first;
	listint_t *second;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	first = list->next;
	second = list->next->next;

	while (first != NULL && second != NULL && second->next != NULL)
	{
		if (first == second)
		{
			return (1);
		}
		first = first->next;
		second = second->next->next;
	}
	return (0);
}
