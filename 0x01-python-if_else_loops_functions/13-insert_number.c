#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts number in a sorted singly-linked list.
 * @head: a pointer the head of hte linked list
 * @number: to be inserted
 * Return: 0 if function fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (node == NULL || node->n >= number)
	{
		newNode->next = node;
		*head = newNode;
		return (newNode);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	newNode->next = node->next;
	node->next = newNode;

	return (newNode);
}
