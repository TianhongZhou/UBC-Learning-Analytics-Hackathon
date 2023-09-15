import pandas
# from matplotlib import pyplot as plt

navigation_events = pandas.read_csv("../data/navigation_events.csv")
assignments = pandas.read_csv("../data/additional/assignments.csv")
discussion_topics = pandas.read_csv("../data/additional/discussion_topics.csv")
discussion = pandas.read_csv("../data/additional/discussions.csv")
enrollments = pandas.read_csv("../data/additional/enrollments.csv")
files = pandas.read_csv("../data/additional/files.csv")
gradebook = pandas.read_csv("../data/additional/gradebook.csv")
module_items = pandas.read_csv("../data/additional/module_items.csv")
pages = pandas.read_csv("../data/additional/pages.csv")

total_time = enrollments.sort_values(by=["user_id"]).drop(index=34)["total_activity_time"]
score = gradebook.sort_values(by=["Student"]).drop(index=0).drop(index=1)["Current Score"]
# for i in range(len(score)):
#     score.iloc[i] = float(score.iloc[i])
# plt.scatter(total_time, score)
# plt.xlabel("Total Activity Time")
# plt.ylabel("Current Score")
# plt.title("Total Activity Time vs Current Score")
# for i in range(score.shape[0]):
#     print("{x: " + str(total_time.iloc[i]) + ",y: " + str(score.iloc[i]) + "},")
# print(enrollments.sort_values(by=["user_id"])["total_activity_time"])
# print(enrollments.sort_values(by=["user_id"]).drop(index=34))
# print(gradebook.sort_values(by=["Student"]).drop(index=0).drop(index=1)["Current Score"])


# print(module_items["title"].value_counts())
mod_names = module_items.drop_duplicates(subset=["title"])["title"].tolist()
nav_mod_data = navigation_events.loc[navigation_events["event__object_extensions_asset_name"].isin(mod_names)]

temp = module_items.drop_duplicates(subset=["title"])
mod_three_data = temp.loc[temp["module_position"]==3]["title"].tolist()
# print(mod_three_data)
# print(nav_mod_data)

# Split navigation events based on "title" in module_items
# for i in range(len(mod_three_data)):
#     temp = nav_mod_data.loc[nav_mod_data["event__object_extensions_asset_name"] == mod_three_data[i]]
#     if len(temp) != 0:
#         temp_name = "module_3_" + str(i) + ".csv"
#         temp = temp.to_csv(temp_name)

discussion_1 = pandas.read_csv("module_3_1.csv")
week1 = discussion_1.sort_values(by=["event_time"]).loc[(discussion_1["event_time"] >= "2033-05-15") & (discussion_1["event_time"] < "2033-05-25")]
print(week1)
