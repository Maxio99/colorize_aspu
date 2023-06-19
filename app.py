# from flask import Flask, request, jsonify, render_template
# import werkzeug
# from werkzeug import utils
#
# app = Flask(__name__)
#
# @app.route('/upload', methods=["POST"])
# def upload():
#     if request.method == "POST":
#         image_file = request.files['image']
#         filename = werkzeug.utils.secure_filename(image_file.filename)
#         print("\nReceived image File name : " + image_file.filename)
#         image_file.save("./uploaded_images/" + filename)
#
#         return jsonify({
#             "message": "Image Uploaded Successfully ",
#         })
#
#
# if __name__ == "__main__":
#     app.run()


# from flask import Flask, render_template, request, jsonify
# from PIL import Image
# import os, io, sys
# import numpy as np
# import cv2
# import base64
#
# app = Flask(__name__)
#
#
# @app.route('/maskImage', methods=['POST'])
# def mask_image():
#     # print(request.files , file=sys.stderr)
#     file = request.files['image'].read()
#     np_img = np.fromstring(file, np.uint8)
#     img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
#     img = Image.fromarray(img.astype("uint8"))
#     raw_bytes = io.BytesIO()
#     img.save(raw_bytes, "JPEG")
#     raw_bytes.seek(0)
#     img_base64 = base64.b64encode(raw_bytes.read())
#     return jsonify({'status': str(img_base64)})
#

from flask import send_file, Flask, request, jsonify
import werkzeug
from werkzeug import utils
import asyncio

app = Flask(__name__)


@app.route('/', methods=["POST"])
async def get_image():
    try:
        image_file = request.files['image']
        filename = werkzeug.utils.secure_filename(image_file.filename)
        file_path = "./uploaded_images/" + filename
        print("\nReceived image File name : " + image_file.filename)
        image_file.save(file_path)
    except Exception:
        return "Failed"
    finally:
        print(file_path)
        return send_file(path_or_file='./uploaded_images/image_picker3556943388527628199.jpg', mimetype='image/png')
if __name__ == "__main__":
    app.run()

# import heapq
#
#
# def heuristic(a, b):
#     # Calculate the Manhattan distance between two points
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])
#
#
# def a_star(start, goal, graph):
#     # Create a priority queue and add the starting node to it
#     frontier = [(0, start)]
#     # Create a dictionary to keep track of the cost of each node
#     cost_so_far = {start: 0}
#     # Create a dictionary to keep track of the previous node in the path
#     came_from = {start: None}
#
#     while frontier:
#         # Get the node with the lowest cost from the priority queue
#         _, current = heapq.heappop(frontier)
#
#         # If we've reached the goal, return the path
#         if current == goal:
#             path = []
#             while current != start:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             path.reverse()
#             return path
#
#         # Check each neighbor of the current node
#         for neighbor in graph[current]:
#             # Calculate the cost to get to this neighbor
#             new_cost = cost_so_far[current] + graph[current][neighbor]
#             # If we haven't seen this neighbor before or the new cost is less than the previous cost
#             if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
#                 # Update the cost and priority of the neighbor
#                 cost_so_far[neighbor] = new_cost
#                 priority = new_cost + heuristic(goal, neighbor)
#                 # Add the neighbor to the priority queue
#                 heapq.heappush(frontier, (priority, neighbor))
#                 # Update the previous node in the path
#                 came_from[neighbor] = current
#
#     # If we've exhausted all possible paths and haven't found the goal, return None
#     return None
