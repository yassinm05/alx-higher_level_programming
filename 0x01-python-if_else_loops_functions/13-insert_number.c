#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: is the int value
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (node == NULL || new->n < node->n)
	{
		new->next = node;
		*head = new;
		return (*head);
	}
	while (node)
	{
		if (node->next == NULL || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
