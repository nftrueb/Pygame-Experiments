import cv2

def main(): 
    cards = cv2.imread('./sprites/playingCards.png')
    width, height = cards.shape[:2]
    print(cards.shape)
    # card_w, card_h = 61, 80
    # rows,cols = 4, 13
    # for i in range(rows): 
    #     start_y= card_h * i
    #     cv2.imwrite('./sprites/ace{num}.jpg'.format(num=str(i)),
    #         cards[start_y:start_y+card_h, :card_w])

if __name__ == '__main__': 
    main()