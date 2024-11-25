class iPhone:
    def __init__(self, name, version, phone_number, color, model):  # constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []
  
    def check_messages(self):
        pass

    def call(self, number):
        pass

    def airdrop(self, filename, recipient):
        print("Dropping %s" % filename)
        pass

    def airreceive(self):
        pass
 
    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Name must be longer than 3 character")
        self.name = new_name

    def send_message(self, recipient, message):
        recipient.receive_message(f"From {self.name}: {message}")

    def receive_message(self, message):
        self.messages.append(message)

    def check_messages(self):
            print(f"Messages on {self.name}:")
            for msg in self.messages:
                print(msg)


# Create 2 instances of iPhone

# Create first instance of iPhone class
first_iphone = iPhone(
    name="Display_iPhone",
    version="18",
    phone_number="123-123-1232",
    color="grey",
    model="iPhone 16 Pro",
)

# Create second instance of iPhone class
second_iphone = iPhone(
    name="Sample_iPhone",
    version="18",
    phone_number="246-246-2524",
    color="white",
    model="iPhone 14",
)
print (first_iphone.name)
print (second_iphone.name)

# Change iPhone names
first_iphone.set_name("Cherry's iPhone")
second_iphone.set_name("Harsh's iPhone")

print ("After name change")

print (first_iphone.name)
print (second_iphone.name)

# Send a message from phone1 to phone2
first_iphone.send_message(second_iphone, "Hi Harsh, how are you?")

# Check messages on phone2
second_iphone.check_messages()