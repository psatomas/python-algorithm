#1. The volume of a sphere with radius r is 34 πr3 . What is the volume of a sphere with radius 5?
sphere_radius = 5
sphere_volume = (4/3) * 3.14159 * sphere_radius**3
print("Sphere volume with radius", sphere_radius, "is", sphere_volume)


# # 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
# $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
# 60 copies?
discount = 0.4
shipping_first_copy = 3.00
shipping_additional_copy = 0.75
number_of_copies = 60   

discounted_price = book_price * (1 - discount)
total_book_cost = discounted_price * number_of_copies
total_shipping_cost = shipping_first_copy + shipping_additional_copy * (number_of_copies - 1)
total_cost = total_book_cost + total_shipping_cost  
print(f"Total cost for {number_of_copies} copies: ${total_cost:.2f}")


# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
easy_pace_seconds = 8 * 60 + 15
tempo_pace_seconds = 7 * 60 + 12
total_run_seconds = (1 * easy_pace_seconds) + (3 * tempo_pace_seconds) + (1 * easy_pace_seconds)
start_time_seconds = (6 * 3600) + (52 * 60)
finish_time_seconds = start_time_seconds + total_run_seconds   

finish_hours = finish_time_seconds // 3600
finish_minutes = (finish_time_seconds % 3600) // 60
finish_seconds = finish_time_seconds % 60
print(f"Finish time: {int(finish_hours)}:{int(finish_minutes):02}:{int(finish_seconds):02} am")

