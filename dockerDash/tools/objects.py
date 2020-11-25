class image_object:
    def __init__(self, Containers, Created, Id, Labels, ParentId, RepoDigests, RepoTags, SharedSize, Size, VirtualSize):
        self.Containers = Containers
        self.Created = Created
        self.Id = Id
        self.Labels = Labels
        self.ParentId = ParentId
        self.RepoDigests = RepoDigests
        self.RepoTags = RepoTags
        self.SharedSize = SharedSize
        self.Size = Size
        self.VirtualSize = VirtualSize

    def __str__(self):
        return f"Image Object -  ID: [{self.Id}]"
