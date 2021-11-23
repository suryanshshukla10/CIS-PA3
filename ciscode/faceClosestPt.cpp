void Mesh::faceClosestPt(size_t           faceIndex,
                         const glm::vec3& pt,
                         glm::vec3&       closePt,
                         float&           bestSqDist) const
{
  const Face&      face       = mFaces.at(faceIndex);
  const glm::vec3& va         = mVertices.at(face.a);
  const glm::vec3& fnorm      = faceNormal(faceIndex);
  glm::vec3        projection = fnorm * glm::dot((va - pt), fnorm);

  float planeDistSq = glm::length2(projection);
  if (planeDistSq > bestSqDist)
    return;

  glm::vec3 projected = pt + projection;

  uint8_t nOutside = 0;
  for (uint8_t i = 0; i < 3; i++) {
    const glm::vec3& v1 = mVertices.at(face.indices[i]);
    const glm::vec3& v2 = mVertices.at(face.indices[(i + 1) % 3]);
    bool outside = glm::dot(glm::cross(v1 - projected, v2 - projected), fnorm) < 0.0f;
    if (outside) {
      nOutside++;
      glm::vec3 ln = v2 - v1;
      float     param =
        std::clamp(glm::dot(ln, projected - v1) / glm::length2(ln), 0.0f, 1.0f);
      glm::vec3 cpt    = v2 * param + v1 * (1.0f - param);
      float     distSq = glm::length2(cpt - pt);
      if (distSq < bestSqDist) {
        closePt    = cpt;
        bestSqDist = distSq;
      }
    }

    if (nOutside > 1)
      break;
  }

  if (nOutside == 0) {
    closePt    = projected;
    bestSqDist = planeDistSq;
  }
}