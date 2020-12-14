# subnet_calculator
A simple subnetting tool for gathering information from CIDR notation. 

The formula for drawing the subnet mask from the number of unique IP addresses comes from this article: 
https://community.spiceworks.com/topic/1838568-the-easy-way-to-calculate-ipv4-subnets-in-your-head

The elif checks in the second half are missing a ".0" because it is already added by python due to the result of the math being a float. 

--ndurand1
