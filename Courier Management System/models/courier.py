# models/courier.py

class Courier:
    def __init__(self, courierID=None, senderName=None, senderAddress=None,
                 receiverName=None, receiverAddress=None, weight=0.0,
                 status="yetToTransit", trackID=None, deliveryDate=None, userId=None):
        self.courierID = courierID
        self.senderName = senderName
        self.senderAddress = senderAddress
        self.receiverName = receiverName
        self.receiverAddress = receiverAddress
        self.weight = weight
        self.status = status
        self.trackID = trackID
        self.deliveryDate = deliveryDate
        self.userId = userId

    def __str__(self):
        return (f"Courier(ID: {self.courierID}, Sender: {self.senderName}, "
                f"Receiver: {self.receiverName}, Weight: {self.weight}, "
                f"Status: {self.status}, Tracking Number: {self.trackID})")
