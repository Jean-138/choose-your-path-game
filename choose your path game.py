print("welcome to the dungeon")

way = input("which way do you want to go?, left or right " )
if way == "right":
     print(" you choose the wrong way, game over ! ")
elif way == "left":
     waterfall =input(" you see a waterfall, do you want to swim or wait ? ")
     if waterfall == "swin":
          print("you try to swin but you did not make it, game over ! ")
     elif waterfall == "wait":
          exit =input("you found a way out, which one you will pick ? the hole, the  door or the rope ? ")
          if exit == "hole":
               print(" ops, wrong way, you are falling ..... game over ")
          elif exit == "rope":
               print("you almost did it, but the rope is  broken, game over ")
          else:
               print(" wooooow, you make it, the door was the only way out, you won the game ")
               
