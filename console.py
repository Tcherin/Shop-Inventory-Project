import pdb
from models.video import Video
from models.supplier import Supplier

import repositories.video_repository as video_repository
import repositories.supplier_repository as supplier_repository

video_repository.delete_all()
supplier_repository.delete_all()

supplier1 = Supplier("VIDEOS R US", "0776494323", True)
supplier_repository.save(supplier1)
supplier2 = Supplier("WE STILL SELL EM VIDEOS", "0774356323", False)
supplier_repository.save(supplier2)
supplier3 = Supplier("VH Yes!", "0774593827", True)
supplier_repository.save(supplier3)

supplier_repository.select_all()

video_1 = Video("Jaws", "Horror", "Hero shark gets cancelled for being too 'real'.", 10, 2, 5, supplier1)
video_repository.save(video_1)
video_2 = Video("Batman Begins", "Superhero", "Billionaire beats the underprivileged because bat.", 15, 2, 5, supplier2)
video_repository.save(video_2)
video_3 = Video("Titanic", "Romance", "Everyone enjoys an ice-bucket challenge", 20, 2, 5, supplier1)
video_repository.save(video_3)
video_4 = Video("Inception", "Thriller", "Just sleeping basically", 8, 2, 5, supplier2)
video_repository.save(video_4)
video_5 = Video("The Shining", "Horror", "Airbnb gone wrong.", 13, 2, 5, supplier3)
video_repository.save(video_5)




pdb.set_trace()