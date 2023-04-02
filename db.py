# This file is for reading data from the db/ directory
import sqlite3
from pprint import pprint


# parses text files (only) found in the db directory
def parse_text(filename):
    FILE_PATH = "data/" + filename
    with open(FILE_PATH,"r") as f:
        data = f.read()
        f.close()
    processed_data = data.split("\n\n\n")
    return processed_data

def connect():
    FILE_PATH="data/tables.db"
    db = sqlite3.connect(FILE_PATH) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    return (c, db)

def disconnect(db):
    db.commit() #save changes
    db.close()  #close database

def add_entry_cite(website,apa):
    c,db = connect()
    c.execute(f"INSERT INTO CITATIONS (WEBSITE, APA) VALUES(?,?)",(website,apa))
    disconnect(db)

def add_entry_resource(link,name,description,category):
    c,db = connect()

    if category == None:
        c.execute(f"INSERT INTO RESOURCES (LINK,NAME,DESC) VALUES(?,?,?)",(link,name,description))
    else:
        c.execute(f"INSERT INTO RESOURCES (LINK,NAME,DESC,CATEGORY) VALUES(?,?,?,?)",(link,name,description,category))

    disconnect(db)

def get_citations():
    c,db = connect()
    citations = c.execute(f"SELECT * FROM citations").fetchall()
    disconnect(db)
    return citations

def get_resources():
    c,db = connect()
    resources = c.execute(f"SELECT * FROM resources").fetchall()
    disconnect(db)
    return resources

if __name__ == "__main__":

    # link, name, description, category
    overall = [
        ["https://www.youtube.com/watch?v=bBC-nXj3Ng4&t=433s",'How does Bitcoin work','This video goes over all of the broad concepts of blockchain in a very similar manner that I did in. The youtuber goes through the steps of converting a ledger into a blockchain and then showing how bitcoin is similar to this. 25 minutes long, but extremely worth it'],
        ["https://www.youtube.com/watch?v=_160oMzblY8","Visual demo of a blockchain","This video goes more into the details of how hashes are created and how each block is linked to the next using a visual diagram. This video really helped me understand what exactly a block was and what information could be stored inside. 18 minutes, but very helpful"],
        ["https://www.youtube.com/watch?v=xIDL_akeras&t=414s",'Public/private key cryptography in Blockchains',"This video shows the interaction between the keys and how people can sign a message or transaction to prove that it is really them. It really helped me understand how this signature works and how it interacts with the greater blockchain system. It is only 9 minutes long and explains one of the hardest things to grasp in blockchain technology (at least for me)"],
        [f'''https://www.simplilearn.com/tutorials/blockchain-tutorial/blockchain-technology#:~:text=A%20blockchain%20platform%20is%20a,consensus%20among%20the%20network%20participants.''',"What is blockchain","Article describing what blockchain is, how it works, and what it can be used for. It is a really brief overview and not the easiest read if its the first thing you look at. I used it to start getting acclimated to the terminology and start figuring out what is referred to by the word “blockchain”. 20 minute read and not that important to go from start to finish, good for skimming over. "],
        ["https://bitcoin.org/bitcoin.pdf","Original white page for Bitcoin","This is the original report created by Satoshi Nakamoto, the inventor of bitcoin, that describes the challenges that bitcoin solves and how the Proof of Work system will work. It also shows how difficult it is to try and tamper with the blockchain using a Binomial Random Walk probability proof. It is a difficult read, it took me more than an hour (>1 hour) to dissect, but if you understand all of the concepts already it can just be an interesting read"],
    ]

    ECDSA = [
        ["https://www.youtube.com/watch?v=dCvB-mhkT0w","Elliptic Curve Cryptography Introduction","This video goes over what the ECDSA system is based on and generally how it works. It does not make clear how the private and public keys have an irreversible cryptographic link, but it is simple to follow. 12 minutes and easy to follow if you want to go deeper into how ECDSA actually works.","signature"],
        ["https://www.youtube.com/watch?v=yBr3Q6xiTw4","Deep dive into the math of ECDCA","This is a deep mathematical dive into the algorithm and how it works. If you're willing to follow along the entire time as he explains proofs and mathematical operations, this video is good for getting a deep dive into how this really works. 30 minutes and not important for understanding blockchain, but still cool.","signature"],
        ["https://www.youtube.com/watch?v=wpLQZhqdPaA","Blockchain specific ECDSA description","This video goes over how blockchain uses this cryptographic function specifically. Instead of going over it theoretically, the video focuses on the practical use of it in bitcoin and how the pairs are generated and related. 20 minutes and good for explaining how it works in blockchains specifically.","signature"],
        ["https://www.mathsisfun.com/algebra/vectors-dot-product.html","Visual demonstration of dot product","This is a short webpage to show what exactly a dot product is, how you can find it (both graphically and algebraically), and its uses. This site is a 5 minute read and shows pretty clearly what the dot product is","signature"]
    ]

    Pow = [
        ["https://developer.bitcoin.org/devguide/block_chain.html#proof-of-work","Bitcoin definition of Proof of Work","This is a short section of the bitcoin documentation that describes what proof of work is and how it works. It goes over why it is needed, what exactly it entails, but does not go into the details and the math. It is a 5 minute read and is good if you’re just a little confused, but it's not very helpful if you have no idea what proof of work is","pow"],
        ["https://www.youtube.com/watch?v=XLcWy1uV8YM","Simply put what is Proof of Work","This video goes over the main concept of proof of work and also does a pretty good job of explaining how it counters many methods of tampering. It also demonstrates why it is needed in a blockchain. 10 minute video that goes over the broad concept of proof of work.","pow"],
    ]

    pos = [
        ["https://www.thebalancemoney.com/what-is-proof-of-stake-pos-5196135","What is Proof of Stake (and comparison to other proofs)","This article describes what proof of stake is and then compares it to proof of work. It also has a comprehensive list of pros and cons. Very simple 15 minute read and gives a good introduction to both proof of work and stake as well as many other less popular proofs.","pos"],
        ["https://www.youtube.com/watch?v=M3EFi_POhps","How does Proof of Stake work","This video is a very simple and boiled down explanation of PoS. It goes over the key concepts and the pros and cons. I like it because it is a visual way of seeing how the validators actually go about validating blocks. It also has a good explanation of the issues and advantages of this proof as well. 8 minute watch that gives a basic breakdown of the concept.","pos"],
        ["https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/","Ethereum specific PoS algorithm","This section from the Ethereum documentation gives an in depth explanation of what proof of stake actually is. It breaks down the steps taken in the proof of stake validation process and explains why it is so hard to tamper with this version of proof of stake. It also goes over the pros and cons of the Etherium implementation. 20 minute read that explains how Ethereum does PoS.","pos"]
    ]

    uses = [
        [f"https://www.ibm.com/topics/smart-contracts#:~:text=Smart%20contracts%20are%20simply%20programs,intermediary's%20involvement%20or%20time%20loss.","Smart Contracts and their uses","This article discusses the current and possible future uses of the blockchain, specifically smart contracts. It also gives a short explanation of what smart contracts are and how they work. What I like about it is that it talks about the specific uses in different industries such as logistics and commerce, however it does not dive deep into how those smart contracts are implemented. It is a 5 minute read on what blockchains are currently being used for."]
    ]

    implement = [
        ["https://www.youtube.com/watch?v=befUVytFC80","How to make your own cryptocurrency token","This video is an in depth tutorial on how you can make your own crypto token. It is a really well made video that defines what a token is, explains the advantages and possibilities of a token, and then actually shows how someone could make a token and make it usable. A 43 minute video, but if you're interested in making your own token, it's one of the clearest free videos available."],
        ["https://www.dappuniversity.com/articles/blockchain-tutorial","Creating a blockchain application (how to)","This article (and the accompanying video) is a tutorial for how to implement an already existing blockchain into your application. The article shows what applications can benefit from blockchain technology by building one. It is a comprehensive guide if you're really trying to get into Web3 development. I would recommend following the video and then use the article to clarify. The video is 2 hours and 45 minutes, but if youre interested in this field then it is a great resource."],
        ["https://ethereum.org/en/developers/docs/","Ethereum documentation","This article (or series of articles) is documentation for how to interact with the Ethereum blockchain. They offer many tutorials and I would recommend you use that because it really doesnt give a clear explanation on how to start or why any of it may be useful. You can spend hours looking at the documentation."],
        ["https://trufflesuite.com/docs/truffle/"," A development environment for blockchain","This is the homepage for a development environment that has many libraries to interact with the blockchain. The documentation is fairly clear and easy to follow, it is just hard to understand how to start. I would recommend watching the above mentioned almost 3 hour tutorial since it utilizes this development environment. You can spend hours looking at the documentation."]
    ]

    # for filling in data the first time
    data = overall + ECDSA + Pow + pos + uses + implement
    # pprint (data)

    for r in data:
        if len(r) == 4:
            add_entry_resource(r[0],r[1],r[2],r[3])
        else:
            add_entry_resource(r[0],r[1],r[2],None)


    pprint(get_resources())