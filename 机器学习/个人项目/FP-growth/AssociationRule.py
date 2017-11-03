import FP_growth


def generateRules(freqItems, freqItemsDict, itemSet,Rule,minConf=0.7):
    for freqItem in freqItems: # freqItem : {'t', 'y', 'x'}
        if len(freqItem) > 1:
            for e in freqItem:
                item = set([e]) | itemSet  #item 为后件
                conf = freqItemsDict[frozenset(freqItem)]/freqItemsDict.get(frozenset(freqItem-item),100)
                if conf >= minConf:
                    Rule[frozenset(freqItem-item)] = [item,conf]
                    generateRules(freqItem-item,freqItemsDict,item,minConf)

if __name__ == "__main__":
    freqItems,freqItemsDict = FP_growth.fpGrowth()  #生成频繁项集  [{a,b},{b,c}...]
    succedent = set([])
    res = {}
    generateRules(freqItems,freqItemsDict,succedent,res)
    print(res)