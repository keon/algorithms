def subarray_with_max_product(arr)
	len = arr.length
	product_so_far = max_product_end = 1
	max_start_i = 0
	so_far_start_i = so_far_end_i = 0

	(0..len-1).each do |i|
		max_product_end *= arr[i]

		if max_product_end < 0
			max_product_end = 1
			max_start_i = i + 1
		end

		if product_so_far < max_product_end
			product_so_far = max_product_end
			so_far_end_i = i
			so_far_start_i = max_start_i
		end
	end
	puts "max_product_so_far: #{product_so_far}, #{arr[so_far_start_i..so_far_end_i]}"
end

# example: 
# subarray_with_max_product([2,3,6,-1,-1,9,5])
# max_product_so_far: 45, [9, 5]
