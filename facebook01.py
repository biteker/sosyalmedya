import facebook

graph = facebook.GraphAPI(access_token='EAACEdEose0cBADVi4AeKpZCz1bza3UhzzG2IPdsxgQMepofLb2tfzZCOmxly5QMJwIp5qVWeaVZAar4Pxl3FBDQzeIBGNz6ls2bzdwj8kW0QWjTLJXvSFMVLINVAZCXwjyo9nlOx3RYEZANM2fz1tYZA28JNq4XOY2aX2GOfPq923hNG6VX7zlIhT5ODEjwF4ZD', version='2.7')
friends = graph.get_connections(id='me', connection_name='friends')
print friends["summary"]["total_count"]
