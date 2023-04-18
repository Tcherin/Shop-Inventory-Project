import pdb
from models.video import Video
from models.supplier import Supplier

import repositories.video_repository as video_repository
import repositories.supplier_repository as supplier_repository

video_repository.delete_all()
supplier_repository.delete_all()

supplier_1 = Supplier("VIDEOS R US", "0776494323", True)
supplier_repository.save(supplier_1)
supplier_2 = Supplier("We still got em videos", "0774356323", False)
supplier_repository.save(supplier_2)
supplier_3 = Supplier("VH Yes!", "0774593827", True)
supplier_repository.save(supplier_3)

supplier_repository.select_all()

video_1 = Video("Jaws", "Horror", "Hero shark gets cancelled for being too 'real'.", 10, 2, 5, supplier_1)
video_repository.save(video_1)
video_2 = Video("Batman Begins", "Superhero", "Billionaire beats the underprivileged because bat.", 15, 2, 5, supplier_2)
video_repository.save(video_2)
video_3 = Video("Titanic", "Romance", "Everyone enjoys an ice-bucket challenge.", 20, 2, 5, supplier_1)
video_repository.save(video_3)
video_4 = Video("Inception", "Thriller", "Just sleeping basically.", 8, 2, 5, supplier_2)
video_repository.save(video_4)
video_5 = Video("The Shining", "Horror", "Airbnb gone wrong.", 13, 2, 5, supplier_3)
video_repository.save(video_5)
video_6 = Video("E.T", "Kids", "Space Uber sucks.", 3, 4, 7, supplier_3)
video_repository.save(video_6)
video_7 = Video("Nightmare on Elm Street", "Horror", "Man teaches kids to believe in their dreams.", 6, 3, 6, supplier_2)
video_repository.save(video_7)
video_8 = Video("Stuart Little", "Kids", "Rich family adopts mouse instead of needy child.", 12, 3, 5, supplier_1)
video_repository.save(video_8)
video_9 = Video("Snow White", "Kids", "Man kisses unconscious woman while seven other guys watch.", 0, 5, 8, supplier_2)
video_repository.save(video_9)
video_10 = Video("Man of Steel", "Superhero", "Illegal alien of temporary use to America.", 12, 3, 6, supplier_3)
video_repository.save(video_10)
video_11 = Video("The Wizard of Oz", "Kids", "Woman commits murder and meets three friends to kill again.", 4, 6, 8, supplier_1)
video_repository.save(video_11)
video_12 = Video("The Sound of Music", "Musical", "Nun bangs her boss and flees the country.", 9, 4, 6, supplier_3)
video_repository.save(video_12)




pdb.set_trace()