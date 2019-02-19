def mod(a)
  if a<0:
    return -a
  else
    return a
end

def mod_add(a, b, c)
	a = mod(a)
	b = mod(b)
	c = mod(c)
	return a+b+c
end

def mod_subtract(a, b, c)
	a = mod(a)
	b = mod(b)
	c = mod(c)
	return a-b-c
end