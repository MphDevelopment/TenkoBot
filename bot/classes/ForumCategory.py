from unidecode import unidecode
class ForumCategory:
  def __init__(self, category_id: str, description_message: ReactionRoleMessage):
    self.category_id = category_id
    self.forums = []
    self.description_message = description_message



class Forum:
  def __init__(self, category_id: str, topic, channel_id, role_id, reaction):
    self.forum_cat = forum_cat
    self.topic = topic
    self.channel_id = channel_id
    self.role_id = role_id
    self.reaction = reaction



class ReactionRoleMessage:
  def __init__(self, channel_id: str, message_id: str, text: str, reaction_to_role: dict = {}):
    self.channel_id = channel_id
    self.message_id = message_id
    self.text = text
    self.reaction_to_role = reaction_to_role

  def add_reaction_role(self, reaction: str, role_id: str):
    if self.reaction_to_role.get(reaction) is not None:
      raise Exception("Reaction is already used")

    self.reaction_to_role.update({ reaction: role_id })

  def remove_reaction_role(self, reaction):
    try:
      del self.reaction_to_role[reaction]
    except KeyError as e:
      print(self, reaction, e)
      raise Exception("No role is linked to this reaction")

  def update_text(text: str):
    self.text = text



class ForumService():
  # ...
  # Everything TODO here basically just ideas, syntax is probably wrong
  def create_forum_cat(self, context, category_name, description, main_channel_name = None):
    new_cat = context.guild.create_category(category_name)
    main_channel = new_cat.create_text_channel(main_channel_name or f"{unidecode(category_name)}-home")
    description_message = main_channel.send_message(..description..)

    forum_cat = ForumCategory(new_cat.id,
      ReactionRoleMessage(main_channel.id, description_message.id, description))

    db.write_forum_cat(forum_cat)
    return forum_cat


  def create_forum(self, context, category_id, topic, reaction, channel_name = None, role_name = None):
    forum_cat = self.get_forum_cat_by_id(context.guild.id, category_id)
    channel = forum_cat.create_text_channel( channel_name or unidecode(topic) )
    role = context.guild.create_role(...., role_name or topic)
    channel.setPermissions({everyone = "no read access", role = "read_access")

    new_forum = Forum(category_id, topic, channel.id, role.id, reaction)
    forum_cat.add_forum(new_forum)

    self.refresh_forum_category(forum_cat)

    return forum







