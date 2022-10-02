# A node in a trie has an interface name, which could be None, left and right nodes, which 
# could also be None, and a parent
class Node():
	def __init__(self, interface_name, left, right, parent):
		self.interface_name = interface_name
		self.left = left
		self.right = right


	# Recursively add a new interface_name to prefix mapping (e.g., P0, 11*) to this node
	def add(self, interface_name, prefix):
		# This is the base case - since all prefixes end in *, if we find the * character,
		# just add the interface name to the node
		if prefix == "*":
			self.interface_name = interface_name
		else:
			# Otherwise, branch left or right depending on whether we find a 0 or 1
			if prefix[0] == '0':
				# If left node doesn't exist, create it 
				if self.left is None:
					new_node = Node(None, None, None, self)
					self.left = new_node

				# We've already looked at the first character, so let's remove the first character
				# and tell our left node to add what's remaining of the prefix
				self.left.add(interface_name, prefix[1:])
			elif prefix[0] == '1':
				# If right node doesn't exist, create it
				if self.right is None:
					new_node = Node(None, None, None, self)
					self.right = new_node

				# We've already looked at the first character, so let's remove the first character
				# and tell our right node to add what's remaining of the prefix
				self.right.add(interface_name, prefix[1:])


	# Implement this function
	def lookup(self, IP_string, best_match):
		#if we have reached the end of the string, then we return best_match
		if self.interface_name != None:
			best_match = self.interface_name
		if IP_string == '':
			return best_match
		if IP_string[0] == '0':
			# if left node doesn't exist, return current best_match,
			if self.left == None:
				return best_match
			# else we update with newest longest correct prefix.
			else:
				return self.left.lookup(IP_string[1:], best_match)
		else:
			# if right node doesn't exist, return current best_match,
			if self.right == None:
				return best_match
			# else we update with newest longest correct prefix.
			else:
				return self.right.lookup(IP_string[1:], best_match)

# The trie class is initiliazed with a root node
class Trie():
	def __init__(self, root):
		self.root = root

	# Add to trie by adding it to the root
	def add(self, interface_name, prefix):
		self.root.add(interface_name, prefix)


	# Lookup an IP address in a trie by starting the lookup at the root
	def lookup(self, IP_string):
		return self.root.lookup(IP_string, None)


def main():
	# Create a root node and our trie
	root_node = Node(None, None, None, None)
	t = Trie(root_node)

	# Read in and add prefixes from the txt file
	prefixes = "prefixes.txt"
	with open(prefixes, "r") as file:
	    for i in file.readlines():
	        entry = i.strip().split(",")
	        try:
	            t.add(entry[0], entry[1])
	        except:
	        	pass

	# Results: report which interface (e.g., P1, P2) each of the following IP addresses is sent to
	# 1
	assert(t.lookup("01101000101001111010001101011000") == 'P10')

	# 2
	print(t.lookup("10010100011100011100100100101111"))

	# 3
	print(t.lookup("10010100011100011100111010100010"))

	# 4
	print(t.lookup("00010101010001111100101000111000"))

	# 5
	print(t.lookup("10101010100001111100111010101111"))

if __name__ == '__main__': 
	main()