#!/usr/bin/env python
# coding: utf-8

# In[2]:


import osmnx as ox


# In[3]:


ox.config(use_cache=True, log_console=True)


# In[14]:


graph = ox.graph_from_bbox(48.1510, 48.1249, 11.5430, 11.6104, network_type='walk', simplify=True, retain_all=False)


# In[26]:


fig, ax = ox.plot_graph(graph, node_size=0, edge_color='w', edge_linewidth=0.2, bgcolor='k', figsize=(20, 20), dpi=10000)


# In[24]:


basic_stats = ox.basic_stats(graph)
extended_stats = ox.extended_stats(graph)


# In[18]:


nodes = ox.graph_to_gdfs(graph, nodes=True, edges=False)


# In[25]:


extended_stats

