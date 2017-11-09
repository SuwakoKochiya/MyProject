import FP_growth


def generateRules(freqItemStatic,freqItem, freqItemsDict, itemSet,Rule,minConf=0.9):
 # freqItem : {'t', 'y', 'x'}
    if len(freqItem) > 1:
        for e in freqItem:
            item = set([e]) | itemSet  #item 为后件
            conf = freqItemsDict[frozenset(freqItemStatic)]/freqItemsDict.get(frozenset(freqItemStatic-item),100)
            if conf >= minConf:
                Rule.append([frozenset(freqItemStatic-item),item,conf])
                generateRules(freqItemStatic,freqItemStatic-item,freqItemsDict,item,Rule)

if __name__ == "__main__":
    freqItems,freqItemsDict = FP_growth.fpGrowth()  #生成频繁项集  [{a,b},{b,c}...]
    res = []
    for freqItem in freqItems:
        succedent = set([])
        generateRules(freqItem,freqItem,freqItemsDict,succedent,res)
    print(res)