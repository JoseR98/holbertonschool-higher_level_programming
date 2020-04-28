#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - insert node in sorted linked list
 * @head: pointer to linked list
 * @number: value to insert
 * Return: addres of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	while (temp != NULL)
	{
		if (temp->n < number)
		{
			if (temp->next->n > number)
			{
				new->next = temp->next;
				new->n = number;
				temp->next = new;
			}
		}
		temp = temp->next;
	}
	return (new);
}
