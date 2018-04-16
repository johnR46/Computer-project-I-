def visualize_boxes_and_labels_on_image_array(image,
                                              boxes,
                                              classes,
                                              scores,
                                              category_index,
                                              instance_masks=None,
                                              keypoints=None,
                                              use_normalized_coordinates=False,
                                              max_boxes_to_draw=20,
                                              min_score_thresh=.5,
                                              agnostic_mode=False,
                                              line_thickness=4):
  """Overlay labeled boxes on an image with formatted scores and label names.

  This function groups boxes that correspond to the same location
  and creates a display string for each detection and overlays these
  on the image. Note that this function modifies the image in place, and returns
  that same image.

  Args:
    image: uint8 numpy array with shape (img_height, img_width, 3)
    boxes: a numpy array of shape [N, 4]
    classes: a numpy array of shape [N]. Note that class indices are 1-based,
      and match the keys in the label map.
    scores: a numpy array of shape [N] or None.  If scores=None, then
      this function assumes that the boxes to be plotted are groundtruth
      boxes and plot all boxes as black with no classes or scores.
    category_index: a dict containing category dictionaries (each holding
      category index `id` and category name `name`) keyed by category indices.
    instance_masks: a numpy array of shape [N, image_height, image_width], can
      be None
    keypoints: a numpy array of shape [N, num_keypoints, 2], can
      be None
    use_normalized_coordinates: whether boxes is to be interpreted as
      normalized coordinates or not.
    max_boxes_to_draw: maximum number of boxes to visualize.  If None, draw
      all boxes.
    min_score_thresh: minimum score threshold for a box to be visualized
    agnostic_mode: boolean (default: False) controlling whether to evaluate in
      class-agnostic mode or not.  This mode will display scores but ignore
      classes.
    line_thickness: integer (default: 4) controlling line width of the boxes.

  Returns:
    uint8 numpy array with shape (img_height, img_width, 3) with overlaid boxes.
  """
  # Create a display string (and color) for every box location, group any boxes
  # that correspond to the same location.
  speed_object = 'speed :'  
  box_to_display_str_map = collections.defaultdict(list)
  box_to_color_map = collections.defaultdict(str)
  box_to_instance_masks_map = {}
  box_to_keypoints_map = collections.defaultdict(list)
  if not max_boxes_to_draw:
    max_boxes_to_draw = boxes.shape[0]
  for i in range(min(max_boxes_to_draw, boxes.shape[0])):
  
    if scores is None or scores[i] > min_score_thresh:
      box = tuple(boxes[i].tolist())
      if instance_masks is not None:
        box_to_instance_masks_map[box] = instance_masks[i]
      if keypoints is not None:
        box_to_keypoints_map[box].extend(keypoints[i])
      if scores is None:
        box_to_color_map[box] = 'black'
      else:
        if not agnostic_mode:
          if classes[i] in category_index.keys():
            class_name = category_index[classes[i]]['name']
          else:
            class_name = 'N/A'
            
          
          # find a center point.
          ymin, xmin, ymax, xmax = box
          ycenter = (ymin + ymax) / 2
          xcenter = (xmin + xmax) / 2
          display_str = '{0:}  ({1:.2f},{2:.2f}) {3:} {4:.3f}'.format(class_name, xcenter, ycenter,speed_object,
          speeds())
          graph('x**-0.0014 + 1.8517*x + 596.37',time.time() - start_time)
          
        
        
        else:
          display_str = 'score: {}%'.format(int(100 * scores[i]))
        box_to_display_str_map[box].append(display_str)
        if agnostic_mode:
          box_to_color_map[box] = 'DarkOrange'
        else:
          box_to_color_map[box] = STANDARD_COLORS[
              classes[i] % len(STANDARD_COLORS)]
  
   


  # Draw all boxes onto image.
  for box, color in box_to_color_map.items():
    ymin, xmin, ymax, xmax = box
    if instance_masks is not None:
      draw_mask_on_image_array(
          image,
          box_to_instance_masks_map[box],
          color=color
      )
    draw_bounding_box_on_image_array(
        image,
        ymin,
        xmin,
        ymax,
        xmax,
        color=color,
        thickness=line_thickness,
        display_str_list=box_to_display_str_map[box],
        use_normalized_coordinates=use_normalized_coordinates)
    if keypoints is not None:
      draw_keypoints_on_image_array(
          image,
          box_to_keypoints_map[box],
          color=color,
          radius=line_thickness / 2,
          use_normalized_coordinates=use_normalized_coordinates)

  return image



# convert ycenter to xpost
def convert_y_to_x(a):
    b = math.sqrt(-0.0056 * a + 6.768465)
    ans_xpost = (1.8517 - b)/0.0028
    print(ans_xpost)
    return ans_xpost

                                                                      
#convert ycenter(t)     
def calculator_y_time(formula,x):
    ans_ydiscount = eval(formula)
    print(ans_ydiscount)
    start_time = time.time()
    return ans_ydiscount

                                                                      

                                                                      

def speeds():
       
    times = time.time()
  
    discount_y_1 = calculator_y_time('x**-0.0014 + 1.8517*x + 596.37',times - start_time) #timestart
    xpost_1 = convert_y_to_x(discount_y_1)


    
    discount_y_2 = calculator_y_time('x**-0.0014 + 1.8517*x + 596.37',time.time() - start_time) #timenow
    xpost_2 = convert_y_to_x(discount_y_2)
    
    V = (xpost_2 - xpost_1) / (time.time() - times)  # xpost_2 - xpost_1  / time_2 - time_1 
    
    print(V)
    return V
    
   

  
def graph(formula,x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x,y)
    plt.xlabel('cout post')
    plt.ylabel('distance of post')
   # plt.show()
