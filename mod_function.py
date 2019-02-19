def mod(a)
  if a<0:
    return -a
  else
    return a
end

def mod_add(a, b)
	a = mod(a)
	b = mod(b)
	return a+b
end

def mod_subtract(a, b)
	a = mod(a)
	b = mod(b)
	return a-b
end