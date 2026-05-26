def d():
    
    try:
      a = int(input("Enter the number : "))

      c = 1/a
      print(c)
    except Exception as e:
      print(e)
    finally:
      print("You have done")

d()
    