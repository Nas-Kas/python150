'''

two stacks
one to keep the back history
one to keep the forward history
one variable to keep the current url

init will be setting the current url to none
and initiailizing both arrays

visit
- clear forward history i.e the forward stack is set to none
- set the current url to whatever url is passed through the param


back_history []

currentUrl = google.com

forward_history []

back move x steps back in history
- move current url to forward history
- pop off from back history and set it as current url
- repeat until our incremented x count is 0 or back history is empty
- return current url


back_history []

currentUrl = google.com

forward_history []

forward 
- move current url to back history
- pop off from forward history and set it to current url
- repeat until our x count is 0 or forward history is empty
- return the current url

'''


class BrowserHistory:

    def __init__(self, homepage: str):
        if homepage is not None:
            self.currentUrl = homepage
        else:
            self.currentUrl = None
        self.back_history = []
        self.forward_history = []


    def visit(self, url: str) -> None:
        if self.currentUrl is not None:
            self.back_history.append(self.currentUrl)
        self.forward_history = []
        self.currentUrl = url
        #print(f"VISIT: forward history {self.forward_history}, backhistory {self.back_history}, currentUrl {self.currentUrl}")
        

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.back_history) > 0:
            self.forward_history.append(self.currentUrl)
            self.currentUrl = self.back_history.pop()
            steps -= 1
        #print(f"BACK: forward history {self.forward_history}, backhistory {self.back_history}, currentUrl {self.currentUrl}")
        return self.currentUrl
        

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.forward_history) > 0:
            self.back_history.append(self.currentUrl)
            self.currentUrl = self.forward_history.pop()
            steps -= 1
        #print(f"FORWARD: forward history {self.forward_history}, backhistory {self.back_history}, currentUrl {self.currentUrl}")
        return self.currentUrl


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)