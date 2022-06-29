#include "lists.h"

/**
 * check_cycle - checks if the linked list contains a cycle
 * @list: head of linked list to check
 * Return: 0 if list has no cycle, 1 if it has
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = malloc(sizeof(listint_t));
	
	if (list == NULL || temp == NULL)
		return (0);

	temp = list;
	while (temp -> next != NULL)
	{
		if (temp -> next == list)
		{
			return (1);
		}
		temp = temp -> next;
	}
	return (0);
}
