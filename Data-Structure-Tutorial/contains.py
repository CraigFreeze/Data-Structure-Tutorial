def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if node == None:
            #Module not found!
            return False
        if node.left is data or node.right is data or data == node.data:
            return True
        elif data < node.data:
            # The data belongs on the left side.
            # Need to keep looking.  Call _contains
            # recursively on the left sub-tree.
            return self._contains(data, node.left)
        else: 
            # The data belongs on the right side.
            # Need to keep looking.  Call _contains
            # recursively on the right sub-tree.
            return self._contains(data, node.right)