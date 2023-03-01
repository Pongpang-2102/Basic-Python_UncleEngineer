# ณ หน้าร้านปิ้งย่างชื่อดังแห่งหนึ่ง ๆ เพื่อน ๆ ทั้ง 4 คนปรึกษากันว่าวันนี้จะกินปิ้งย่างกันให้พุงกาง แค่จะกินเซตไหนดีล่ะ

# Dictionary ข้อมูลเพื่อน ๆ ในกลุ่ม ประกอบด้วย ชื่อ และเงินที่พกมา
team_members = {"Pongpang" : 1800 , "Somchai": 1500 , "Beam" : 1350 , "Somsri" : 910 }

#  สร้าง function รับค่า Dictionary ข้อมูลเพื่อนๆ ในกลุ่ม 
def EatBuffet_or_Not(your_team) :
  
    team_members_money_list = []  # สร้าง empty list เพื่อรับค่าเงินที่เพื่อน ๆ พกมา
    # แยกองค์ประกอบ key กับ value แล้วเอาเฉพาะ value (เงินที่พกมา)
    for  member_name ,member_money in team_members.items()   :
        team_members_money_list.append(member_money)

    min_money = min(team_members_money_list)  # หาค่าเงินที่น้อยที่สุด เพื่อมาคำนวณว่าจะกินเซตไหน (เพราะไม่เลี้ยงแน่นอน )
    print(f"ในพวกเรา คนที่มีเงินน้อยสุดมี {min_money} THB")

    menu_set_wo_vat = {"yakiniku":399 , "premium": 649 ,"prime":849 , "platinum":1099 , "prestige": 1499 , "ultra":1999}
    price_wt_vat = [] # หาค่าเงินที่น้อยที่สุด เพื่อมาคำนวณว่าจะกินเซตไหน (เพราะไม่เลี้ยงแน่นอน )

    for menu_set , price_set in menu_set_wo_vat.items() :
        price_set_with_vat = round((price_set*1.07),2)
        price_wt_vat.append(price_set_with_vat)

    # หาค่าเมนูที่ถูกที่สุด
    min_price = min(price_wt_vat)
    print(f"ในร้านนี้ เมนูที่ถูกสุดอยู่ที่ {min_price} THB")
     
    # กำหนดตัวแปร เพื่อให้เงื่อนไขไม่ยาวมาก เดี๋ยวตาลายครับ
    a,b,c,d,e,f = price_wt_vat[0] ,price_wt_vat[1] , price_wt_vat[2] , price_wt_vat[3] , price_wt_vat[4] , price_wt_vat[5]

    # สร้างเงื่อนไขเปรียบเทียบราคาแต่ละ set กับเงินที่มี (min)
    if  min_money >= min_price : 
        # ป๋าสุด ได้หมด
        if ( (min_money - a ) >= 0 ) and  ( (min_money - b) >= 0 ) and ( (min_money- c) >= 0 ) and  ( (min_money - d) >= 0 ) and ( (min_money- e) >= 0 ) and ( (min_money- f) >= 0 ) :
            print("ได้ทุกเซตเลย เอา Ultra แพงสุดเลยละกัน")
        # ยกเว้นตัวท๊อป
        elif ( (min_money- a ) >= 0 ) and  ( (min_money - b) >= 0 ) and ( (min_money- c) >= 0 ) and  ( (min_money - d) >= 0 ) and ( (min_money- e) >= 0 ) and ( (min_money- f) < 0 ) :
            print("ได้หมดยกเว้นตัวท๊อบ เลือกได้ 5  อัน เอาไรดี")
        # เลือกได้ 4 อัน / ยากิ พรีเมี่ยม ไพร์ม แพลตินัม 
        elif ( (min_money- a ) >= 0 ) and  ( (min_money - b) >= 0 ) and ( (min_money- c) >= 0 ) and  ( (min_money - d) >= 0 ) and ( (min_money- e) < 0 ) and ( (min_money- f) < 0 ) :
            print("เลือกได้ 4  อัน ยากิ พรีเมี่ยม ไพร์ม แพลตินัม เอาไรดี")
        # เลือกได้ 3 อัน / ยากิ พรีเมี่ยม ไพร์ม 
        elif ( (min_money- a ) >= 0 ) and  ( (min_money - b) >= 0 ) and ( (min_money- c) >= 0 ) and  ( (min_money - d) < 0 ) and ( (min_money- e) < 0 ) and ( (min_money- f) < 0 ) :
            print("เลือกได้ 3  อัน ยากิ พรีเมี่ยม ไพร์ม  เอาไรดี")
        # เลือกได้ 2 อัน / ยากิ พรีเมี่ยม 
        elif ( (min_money- a ) >= 0 ) and  ( (min_money - b) >= 0 ) and ( (min_money- c) < 0 ) and  ( (min_money - d) < 0 ) and ( (min_money- e) < 0 ) and ( (min_money- f) < 0 ) :
            print("เลือกได้ 2  อัน ยากิ กับ พรีเมี่ยม  เอาไรดี")
        # เงินน้อย กินเซตประหยัดก็ยังดี  
        elif ( (min_money- a ) >= 0 ) and  ( (min_money - b) < 0 ) and ( (min_money- c) < 0 ) and  ( (min_money - d) < 0 ) and ( (min_money- e) < 0 ) and ( (min_money- f) < 0 ) :
            print("เรากินเซต Yakinuku ได้ ไปลุยกันเถอะ")
    # เงินไม่พอ กลับบ้านก่อน
    else :
        print("กลับไปกินข้าวราดแกงข้างหอเถอะพวกเรา")

# ลองถามอับดุลดู ว่าไงก็ตามนั้นแหละ อิอิ
EatBuffet_or_Not(team_members)
